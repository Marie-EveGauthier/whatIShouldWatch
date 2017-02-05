<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * writers
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\writersRepository")
 */
class writers {

    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var string
     *
     * @ORM\Column(name="name", type="string", length=255)
     */
    private $name;

    /**
     * @var string
     *
     * @ORM\Column(name="gender",type="string", length=1, options={"fixed" = true},nullable=true)
     */
    private $gender = NULL;

    /**
     * @var boolean
     *
     * @ORM\Column(name="poc", type="boolean",nullable=true)
     */
    private $poc = NULL;

    /**
     * @var boolean
     *
     * @ORM\Column(name="LGBTQ", type="boolean",nullable=true)
     */
    private $LGBTQ = NULL;

    /**
     * Get id
     *
     * @return integer
     */
    public function getId() {
        return $this->id;
    }

    /**
     * Set name
     *
     * @param string $name
     * @return writers
     */
    public function setName($name) {
        $this->name = $name;

        return $this;
    }

    /**
     * Get name
     *
     * @return string
     */
    public function getName() {
        return $this->name;
    }

    /**
     * Set gender
     *
     * @param string $gender
     * @return writers
     */
    public function setGender($gender) {
        $this->gender = $gender;

        return $this;
    }

    /**
     * Get gender
     *
     * @return string
     */
    public function getGender() {
        return $this->gender;
    }


    /**
     * Set poc
     *
     * @param boolean $poc
     * @return writers
     */
    public function setPoc($poc)
    {
        $this->poc = $poc;
    
        return $this;
    }

    /**
     * Get poc
     *
     * @return boolean 
     */
    public function getPoc()
    {
        return $this->poc;
    }

    /**
     * Set LGBTQ
     *
     * @param boolean $lGBTQ
     * @return writers
     */
    public function setLGBTQ($lGBTQ)
    {
        $this->LGBTQ = $lGBTQ;
    
        return $this;
    }

    /**
     * Get LGBTQ
     *
     * @return boolean 
     */
    public function getLGBTQ()
    {
        return $this->LGBTQ;
    }
}
